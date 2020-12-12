function initialise_storage(){
	console.log("Initialised storage");
	sessionStorage.counter = 1;
	sessionStorage.num_entries = 5; // number of entries per page
	sessionStorage.total = 1; //total number of entries

	while(document.getElementById(String(sessionStorage.total)) != null) {
		sessionStorage.total = parseInt(sessionStorage.total) + 1;
	}
	sessionStorage.total--; //total number of entries

}

function tabulate(){
	console.log(sessionStorage.num_entries);
	console.log(sessionStorage.total);
	let j = 1; // to iterate through the table rows 

	while(j <= sessionStorage.total) {
		if(j<=sessionStorage.num_entries) {
			document.getElementById(String(j)).style.display="table-row";
		}
		else {
			document.getElementById(String(j)).style.display="none";
		}
		j++;
	}
	sessionStorage.counter=1;
}

function re_tabulate(n){
	sessionStorage.num_entries = n;
	tabulate();
}

let prev = document.getElementById('prev_button');
prev.onclick = function() {
	if(sessionStorage.counter > 1) {
		sessionStorage.counter--;
	}

	let i = 1;

	while(i <= sessionStorage.total) {
		if(i <= sessionStorage.counter*sessionStorage.num_entries && i > (sessionStorage.counter-1)*sessionStorage.num_entries) {
			document.getElementById(String(i)).style.display="table-row";
		}
		else {
			document.getElementById(String(i)).style.display="none";
		}
		i++;
	}
}

let next = document.getElementById('next_button');
next.onclick = function() {
	if(sessionStorage.counter*sessionStorage.num_entries < sessionStorage.total) {
		sessionStorage.counter++;
	}

	let i = 1;

	while(i <= sessionStorage.total) {
		if(i <= sessionStorage.counter*sessionStorage.num_entries && i > (sessionStorage.counter-1)*sessionStorage.num_entries) {
			document.getElementById(String(i)).style.display="table-row";
		}
		else {
			document.getElementById(String(i)).style.display="none";
		}
		i++;
	}
}
