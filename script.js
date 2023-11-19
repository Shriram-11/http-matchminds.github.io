document.addEventListener("DOMContentLoaded", function () {
    const selectDateInput = document.getElementById("select-date");
    const calendar = document.getElementById("calendar");

    // Function to update the date input with the selected date from the calendar
    function updateSelectedDate(date) {
        selectDateInput.value = formatDate(date);
        calendar.style.display = "none";
    }

    // Function to format the date as "YYYY-MM-DD"
    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, "0");
        const day = String(date.getDate()).padStart(2, "0");
        return `${year}-${month}-${day}`;
    }

    // Create a simple calendar using the Pikaday library
    const picker = new Pikaday({
        field: selectDateInput,
        format: "YYYY-MM-DD",
        onSelect: updateSelectedDate,
        container: calendar,
        yearRange: [2000, new Date().getFullYear()],
        showYearDropdown: true,
        showMonthDropdown: true,
    });

    // Show the calendar when clicking the date input
    selectDateInput.addEventListener("click", function () {
        calendar.style.display = "block";
    });
    // function showMessage() {
    //     alert("Please refer to the instructions.");
    // }
});
