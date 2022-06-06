import requests
import config

# create mount point

url = "https://app.salsify.com/api/orgs/" + config.id + "/imports/upload_mounts"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + config.sals_api
}

headers2 = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers)
r_json = response.json()

# print(response.text)

# Upload to Mount Point

import_url = "https://salsify-dandelion.s3-external-1.amazonaws.com"

payload = {
    "key": r_json["form_data"]["key"],
    "x-amz-server-side-encryption": r_json["form_data"]["x-amz-server-side-encryption"],
    "acl":  r_json["form_data"]["acl"],
    "policy":  r_json["form_data"]["policy"],
    "x-amz-credential": r_json["form_data"]["x-amz-credential"],
    "x-amz-algorithm": r_json["form_data"]["x-amz-algorithm"],
    "x-amz-date": r_json["form_data"]["x-amz-date"],
    "x-amz-signature": r_json["form_data"]["x-amz-signature"],
    "type": "json_import_format",
    "file": "backup.json"
}

response2 = requests.put(import_url, json=payload, headers=headers2)

print(response2.text)

# Updating an Import to point at a new mount point

upload_url = r_json["url"]

payload2 = {
    "key": r_json["form_data"]["key"],
    "x-amz-server-side-encryption": r_json["form_data"]["x-amz-server-side-encryption"],
    "acl":  r_json["form_data"]["acl"],
    "policy":  r_json["form_data"]["policy"],
    "x-amz-credential": r_json["form_data"]["x-amz-credential"],
    "x-amz-algorithm": r_json["form_data"]["x-amz-algorithm"],
    "x-amz-date": r_json["form_data"]["x-amz-date"],
    "x-amz-signature": r_json["form_data"]["x-amz-signature"],
    "type": "json_import_format",
    "file": "backup.json"
}

response3 = requests.post(upload_url, json=payload2, headers=headers2)

print(response3.text)