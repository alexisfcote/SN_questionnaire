DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd "${DIR}"

git stash
git pull
python3 -m pipenv shell pyinstaller one-file-app.spec
zip dist/SN\ Journal\ de\ bord dist/
