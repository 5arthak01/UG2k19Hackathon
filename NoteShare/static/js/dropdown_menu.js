function toggleClass(elem,className){
    if (elem.className.indexOf(className) !== -1){
      elem.className = elem.className.replace(className,'');
    }
    else{
      elem.className = elem.className.replace(/\s+/g,' ') + 	' ' + className;
    }
  
    return elem;
}

function toggleDisplay(elem){
    const curDisplayStyle = elem.style.display;			

    if (curDisplayStyle === 'none' || curDisplayStyle === ''){
        elem.style.display = 'block';
    }
    else{
        elem.style.display = 'none';
    }

}

function toggleMenuDisplay(e){
    const dropdown = e.currentTarget.parentNode;
    const menu = dropdown.querySelector('.menu');
    const icon = dropdown.querySelector('.fa-angle-right');

    toggleClass(menu,'hide');
    toggleClass(icon,'rotate-90');
}

const dropdownTitle = document.querySelector('.dropdown .title');
dropdownTitle.addEventListener('click', toggleMenuDisplay);
