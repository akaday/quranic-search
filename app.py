from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)
engine = create_engine('postgresql://postgres:admin7@localhost:5432/quran')

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM verses WHERE text_translation ILIKE :keyword"), {'keyword': f'%{keyword}%'}).fetchall()
        verses = []
        for row in result:
            verse = {
                'surah': row[1],  # Assuming surah is the second column
                'ayah': row[2],   # Assuming ayah is the third column
                'text_arabic': row[3],  # Assuming text_arabic is the fourth column
                'text_translation': row[4],  # Assuming text_translation is the fifth column
                'tafsir': row[5]  # Assuming tafsir is the sixth column
            }
            verses.append(verse)
    return jsonify(verses)

if __name__ == '__main__':
    app.run(debug=True)

