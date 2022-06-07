OBJECTIVE

This script should access the Salsify API and upload the backup file (backup.json) which is created by Salsify
automatically. In theory this should restore an entire inventory. Currently configured to a sandbox environment.

1. Script should either automatically download the backup JSON file every so often, OR simply access the already existing script in OneDrive
2. Creates mount point on Salsify API
3. Uploads JSON file to mount point
4. Restores inventory to backed up state.
