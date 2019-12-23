#!/usr/bin/env bash
echo "Good Morning Gamer, what event you need "
read eventCode
curl -X GET "https://www.thebluealliance.com/api/v3/event/$eventCode/teams/simple" -H "accept: application/json" -H "X-TBA-Auth-Key: icVifn1ZDq7vWcwCVvW1tBtTGSVSaQWIRJAzp7O21tQPSBmfK509B8dbKhxyMAF9" | jq '.[]| .team_number' >> results.txt
curl -X GET "https://www.thebluealliance.com/api/v3/event/$eventCode/teams/simple" -H "accept: application/json" -H "X-TBA-Auth-Key: icVifn1ZDq7vWcwCVvW1tBtTGSVSaQWIRJAzp7O21tQPSBmfK509B8dbKhxyMAF9" | jq '.[]|.nickname' >> nicknames.txt
python sqlshit.py
