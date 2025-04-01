# uv run streamlit run app.py --server.runOnSave True
### uv run streamlit run app.py --server.runOnSave True
Installed 36 packages in 188ms

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8502 // 8501
  Network URL: http://172.20.10.2:8502

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog

//
uv venv
source .venv/bin/activate
deactivate
//

ssh -R 7070:localhost:8501  root@nowayno.info

// git

git add .
git commit -m "ign"
git push -u origin main

gh github
gh repo create flaskajax --public --clone
cd flaskajax
git add .
git commit -m "ign"
git push -u origin main

git remote add github https://github.com/andregraunt/pystreamlit

git push github master

            