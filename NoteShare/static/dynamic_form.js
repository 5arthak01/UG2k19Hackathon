function load_courses() {
    console.log("load");
	let sem_choice = document.getElementById('sem');
	let	course_choice = document.getElementById('course');

    sem = sem_choice.value;
    
    fetch('/course/' + sem).then(function(response) {
        response.json().then(function(data) {
            let optionHTML = ''; 
            if(document.title == 'Browse'){
                optionHTML+='<option value="Any">Any</option>';
            }
            for(let course of data.courses) {
                optionHTML += '<option value="' + course.name + '">' + course.name + '</option>';
            }
            course_choice.innerHTML = optionHTML;
        })
    })
}

window.onload=load_courses();
