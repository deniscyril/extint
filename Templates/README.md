source venv/bin/activate
# puis pour compiler le template page1.html avec les données de page1.yaml
# et le mettre dans test.html
python checktpl.py TEMPLATES/page1.html DATA/page1.yaml > test.html

