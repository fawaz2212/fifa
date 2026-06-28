document.addEventListener("DOMContentLoaded", function () {

    const rounds = document.querySelectorAll(".round");

    // Skip the last round (Final)
    for (let r = 0; r < rounds.length - 1; r++) {

        const currentMatches = rounds[r].querySelectorAll(".match");
        const nextMatches = rounds[r + 1].querySelectorAll(".match");

        currentMatches.forEach((match, matchIndex) => {

            const teams = match.querySelectorAll(".team");

            teams.forEach(team => {

                team.style.cursor = "pointer";

                team.addEventListener("click", function () {

                    // Remove winner from both teams
                    teams.forEach(t => t.classList.remove("winner"));

                    // Set clicked team as winner
                    this.classList.add("winner");

                    // Advance to next round if it exists
                    const nextMatch = nextMatches[Math.floor(matchIndex / 2)];

                    if (nextMatch) {

                        const slots = nextMatch.querySelectorAll(".team");

                        const slotIndex = matchIndex % 2;

                        slots[slotIndex].innerHTML = this.innerHTML;
                    }
                });

            });

        });

    }

});