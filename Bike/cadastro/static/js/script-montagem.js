const options = document.querySelectorAll('.options li');
const selectedList = document.querySelector('.selected');
const searchInput = document.getElementById('searchInput');

options.forEach(option => {
    const addButton = option.querySelector('button');
    addButton.addEventListener('click', () => {
        const part = option.getAttribute('data-part');
        const itemName = option.querySelector('span').textContent;
        const itemImgSrc = option.querySelector('img').src;

        const placeholder = document.querySelector(`.placeholder[data-part="${part}"]`);
            
        if (placeholder) {
            const selectedItem = document.createElement('li');

            const itemImg = document.createElement('img');
            itemImg.src = itemImgSrc;
            selectedItem.appendChild(itemImg);

            const itemText = document.createElement('span');
            itemText.textContent = `${part}: ${itemName}`;
            selectedItem.appendChild(itemText);

            const removeBtn = document.createElement('button');
            removeBtn.textContent = '-';
            selectedItem.appendChild(removeBtn);

            selectedList.replaceChild(selectedItem, placeholder);

            option.style.pointerEvents = 'none';
            option.style.backgroundColor = '#ddd';

            removeBtn.addEventListener('click', () => {
                selectedList.replaceChild(placeholder, selectedItem);
                option.style.pointerEvents = 'auto';
                option.style.backgroundColor = '';
            });
            }
        });
    });

    
    searchInput.addEventListener('input', () => {
        const filter = searchInput.value.toLowerCase();
        options.forEach(option => {
            const itemName = option.querySelector('span').textContent.toLowerCase();
            if (itemName.includes(filter)) {
                option.style.display = ''; 
            } else {
                option.style.display = 'none'; 
            }
        });
    });