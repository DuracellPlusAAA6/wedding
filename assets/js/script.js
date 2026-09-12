// Countdown Timer
function updateCountdown() {
    const weddingDate = new Date("September 10, 2027 13:00:00").getTime();
    const now = new Date().getTime();
    const distance = weddingDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerHTML =
        `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

setInterval(updateCountdown, 1000);

// Dynamic Guest Names for RSVP
function addGuestFields() {
    const guestCount = document.getElementById("guest-count").value;
    const guestNamesDiv = document.getElementById("guest-names");
    guestNamesDiv.innerHTML = "";

    if (guestCount > 1) {
        for (let i = 1; i < guestCount; i++) {
            const input = document.createElement("input");
            input.type = "text";
            input.name = `guest-${i}`;
            input.placeholder = `Guest ${i + 1} Name`;
            input.required = true;
            guestNamesDiv.appendChild(input);
        }
    }
}