const displayDepartmentsBtn = document.getElementById('departments');

const displayDepartments = function () {
    const departmentsUrl = displayDepartmentsBtn.getAttribute('data-url');

    fetch(departmentsUrl)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const listItems = data.map(
                department => `<li>${department}</li>`
            ).join('');

            document.querySelector('.wrapper').innerHTML = `<ul class='list'>${listItems}</ul>`;
        })
        .catch(err => console.error('Error fetching data:', err));
}

displayDepartmentsBtn.addEventListener('click', displayDepartments);
