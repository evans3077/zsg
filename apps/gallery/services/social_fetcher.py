import json
import os
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware, now


class SocialFetcher:
    def fetch_latest(self, platform, limit=6):
        if platform == "instagram":
            return self._fetch_instagram(limit=limit)
        if platform == "tiktok":
            return self._fetch_tiktok(limit=limit)
        return []

    def _fetch_instagram(self, limit=6):
        token = os.getenv("INSTAGRAM_ACCESS_TOKEN", "").strip()
        user_id = os.getenv("INSTAGRAM_USER_ID", "").strip()
        if not token or not user_id:
            return []

        endpoint = (
            f"https://graph.instagram.com/{user_id}/media"
            f"?fields=id,caption,media_url,permalink,timestamp,thumbnail_url"
            f"&limit={limit}&access_token={token}"
        )
        payload = self._json_get(endpoint)
        items = []
        for row in payload.get("data", []):
            dt = self._parse_timestamp(row.get("timestamp"))
            media_url = row.get("thumbnail_url") or row.get("media_url") or ""
            items.append(
                {
                    "post_id": str(row.get("id", "")),
                    "caption": (row.get("caption") or "").strip(),
                    "media_url": media_url,
                    "permalink": row.get("permalink") or "",
                    "timestamp": dt,
                }
            )
        return [i for i in items if i["post_id"] and i["permalink"] and i["timestamp"]]

    def _fetch_tiktok(self, limit=6):
        token = os.getenv("TIKTOK_ACCESS_TOKEN", "").strip()
        open_id = os.getenv("TIKTOK_OPEN_ID", "").strip()
        if not token or not open_id:
            return []

        endpoint = "https://open.tiktokapis.com/v2/post/item/list/"
        body = {
            "open_id": open_id,
            "max_count": limit,
            "fields": [
                "id",
                "title",
                "create_time",
                "share_url",
                "cover_image_url",
            ],
        }
        payload = self._json_post(endpoint, body, token=token)
        items = []
        for row in payload.get("data", {}).get("videos", []):
            ts = row.get("create_time")
            if isinstance(ts, str) and ts.isdigit():
                ts = int(ts)
            dt = datetime.fromtimestamp(ts) if isinstance(ts, int) else None
            if dt is not None and dt.tzinfo is None:
                dt = make_aware(dt)
            items.append(
                {
                    "post_id": str(row.get("id", "")),
                    "caption": (row.get("title") or "").strip(),
                    "media_url": row.get("cover_image_url") or "",
                    "permalink": row.get("share_url") or "",
                    "timestamp": dt,
                }
            )
        return [i for i in items if i["post_id"] and i["permalink"] and i["timestamp"]]

    def _json_get(self, url):
        request = Request(url, method="GET")
        try:
            with urlopen(request, timeout=20) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, ValueError):
            return {}

    def _json_post(self, url, body, token=""):
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
        try:
            with urlopen(request, timeout=20) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, ValueError):
            return {}

    def _parse_timestamp(self, value):
        dt = parse_datetime(value or "")
        if dt is None:
            return now()
        if dt.tzinfo is None:
            dt = make_aware(dt)
        return dt
