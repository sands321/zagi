# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --pack-extension=./chrome-plugin --pack-extension-key=./publish/gpt_helper.pem
# timestamp=$(date +"%Y%m%d-%H%M%S")
# zip -j "publish/gpt-helper_$timestamp.zip" chrome-plugin.crx chrome-plugin/manifest.json
# rm ./chrome-plugin.crx
#---
timestamp=$(date +"%Y%m%d-%H%M%S")
zip -r "publish/gpt-helper_$timestamp.zip" chrome-plugin