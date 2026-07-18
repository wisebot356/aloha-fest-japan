#!/usr/bin/env python3
"""Create the live Aloha Fest vendor-interest form in Tally.

This is intentionally a small first-contact form: vendors can express interest
without committing to a booth, price, date, or detailed operational terms.
"""
from pathlib import Path
from uuid import uuid4
import json
import requests

API = "https://api.tally.so/forms"
key_path = Path.home() / ".config" / "tally" / "api_key"
api_key = key_path.read_text().strip()
workspace_id = "w2PBzb"


def block(block_type, group_type, payload):
    return {
        "uuid": str(uuid4()),
        "type": block_type,
        "groupUuid": str(uuid4()),
        "groupType": group_type,
        "payload": payload,
    }


def question(label, placeholder, required=True):
    return [
        block("TITLE", "TITLE", {"safeHTMLSchema": [[label]]}),
        block("INPUT_TEXT", "INPUT_TEXT", {"isRequired": required, "placeholder": placeholder}),
    ]

blocks = [
    block("FORM_TITLE", "TEXT", {
        "title": "アロハ・フェストに出店しませんか？",
        "safeHTMLSchema": [["アロハ・フェストに出店しませんか？"]],
    }),
    block("TEXT", "TEXT", {"safeHTMLSchema": [[
        "ハワイのアロハと、日本の地域のあたたかさが出会う新しい一日をつくりたいと思っています。",
        "<br/><br/>まずは「少し気になる」「話を聞いてみたい」だけでも大歓迎です。"
    ]]}),
]
blocks += question("お店・活動のお名前", "例：〇〇カフェ")
blocks += question("ご担当者さまのお名前", "お名前")
blocks += question("連絡先（電話・メール・Instagram・LINEなど）", "ご連絡しやすい方法を教えてください")
blocks += question("出店・参加のイメージ", "フード、クラフト、音楽、体験など。まだ決めていない場合も大丈夫です。", required=False)
blocks += question("いまのお気持ちは？", "例：詳しく聞きたい／出店を検討したい／まず相談したい")
blocks += question("こんなことができそう／聞いてみたいこと", "自由にどうぞ。空欄でも大丈夫です。", required=False)
blocks.append(block("TEXT", "TEXT", {"safeHTMLSchema": [[
    "<strong>Mahalo! ご興味をありがとうございます。</strong><br/>アロハ・フェストのイメージや次のご相談について、あらためてご連絡します。"
]]}))

payload = {
    "name": "Aloha Fest — 出店者募集",
    "workspaceId": workspace_id,
    "status": "PUBLISHED",
    "blocks": blocks,
}
response = requests.post(API, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, json=payload, timeout=30)
if not response.ok:
    raise SystemExit(f"Tally create failed: HTTP {response.status_code}: {response.text[:800]}")
created = response.json()
form_id = created["id"]
public_url = f"https://tally.so/r/{form_id}"
Path("tally-live-form.json").write_text(json.dumps({"id": form_id, "url": public_url, "name": created.get("name")}, ensure_ascii=False, indent=2))
print(json.dumps({"id": form_id, "url": public_url, "status": created.get("status")}, ensure_ascii=False))
