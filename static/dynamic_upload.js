let sem_choice = document.getElementById('sem');
let	course_choice = document.getElementById('course');

sem_choice.onchange = function() {
	sem = sem_choice.value;

	fetch('/course/' + sem).then(function(response) {
		response.json().then(function(data) {
			let optionHTML = '';
			for(let course of data.courses) {
				optionHTML += '<option value="' + course.name + '">' + course.name + '</option>';
			}
			course_choice.innerHTML = optionHTML;
		})
	})
}
