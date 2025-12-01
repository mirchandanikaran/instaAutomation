import requests
import time
from config import APIToken, IG_USER_ID, CAPTION

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------
ACCESS_TOKEN = APIToken
IG_USER_ID = IG_USER_ID
CAPTION = CAPTION
VIDEO_URL = "https://www.dropbox.com/scl/fi/y6qjv92y1d16nxd81uoqt/download1.mp4?rlkey=jz957nlvj5cmbe6078hjjnqdu&st=5a1796ut&dl=0"  # ✅ direct-download URL

# ---------------------------------------------------
# STEP 1: Upload the Reel
# ---------------------------------------------------
def upload_reel():
    print("🎬 Uploading reel to Instagram Graph API...")

    upload_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
    payload = {
        "media_type": "REELS",         # ✅ correct media type
        "video_url": VIDEO_URL,        # ✅ must be a direct file URL
        "caption": CAPTION,
        "share_to_feed": True,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(upload_url, data=payload)
    result = response.json()
    print("📤 Upload response:", result)

    if "id" in result:
        return result["id"]
    else:
        print("❌ Failed to upload video.")
        return None

# ---------------------------------------------------
# STEP 2: Publish the Reel
# ---------------------------------------------------
def publish_reel(creation_id):
    print("🚀 Publishing reel...")
    publish_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
    payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(publish_url, data=payload)
    result = response.json()
    print("✅ Publish response:", result)

# ---------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------
if __name__ == "__main__":
    creation_id = upload_reel()
    if creation_id:
        print("⏳ Waiting 120 seconds for Instagram to process video...")
        time.sleep(120)
        publish_reel(creation_id)
    else:
        print("❌ Upload failed — check your video URL or permissions.")
