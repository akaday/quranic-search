async function search() {
    const keyword = document.getElementById('keyword').value;
    const response = await fetch(`/search?keyword=${keyword}`);
    const results = await response.json();
    const resultsList = document.getElementById('results');
    resultsList.innerHTML = '';
    results.forEach(verse => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<p>${verse.text_arabic}</p><p>${verse.text_translation}</p><p>${verse.tafsir}</p>`;
        resultsList.appendChild(listItem);
    });
}
