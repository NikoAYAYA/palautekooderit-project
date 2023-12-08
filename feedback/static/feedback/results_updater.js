// Define global variables so eslint shuts up
/* global document, Handlebars, Chart */

let topicSelect = document.getElementById('topicSelect');
let goodFeedback = document.getElementById('good_feedback');
let badFeedback = document.getElementById('bad_feedback');
let ideasFeedback = document.getElementById('ideas_feedback');

let feedbackCardTemplateSource = document.getElementById('feedback-card-template').innerHTML;
let feedbackCardTemplate = Handlebars.compile(feedbackCardTemplateSource);

let ratingChart;

topicSelect.addEventListener('change', function() {
    if (this.value == 'None') return;

    fetch(`/feedback/get-feedbacks/${this.value}`)
        .then(res => res.json())
        .then(feedbacks => {
            let ratingCounts = [0, 0, 0, 0, 0];

            // Clear previous feedbacks
            goodFeedback.innerHTML = '';
            badFeedback.innerHTML = '';
            ideasFeedback.innerHTML = '';

            for (let i = 0; i < feedbacks.length; i++) {
                let feedback = feedbacks[i];
                let fields = feedback['fields']

                ratingCounts[fields['rating'] - 1] += 1;

                let goodFeedbackText = fields['good'];
                let badFeedbackText = fields['bad'];
                let ideasFeedbackText = fields['ideas'];

                if (goodFeedbackText != '') {
                    let goodFeedbackCardHTML = feedbackCardTemplate({ feedback_p: goodFeedbackText });
                    goodFeedback.innerHTML += goodFeedbackCardHTML;
                }

                if (badFeedbackText != '') {
                    let badFeedbackCardHTML = feedbackCardTemplate({ feedback_p: badFeedbackText });
                    badFeedback.innerHTML += badFeedbackCardHTML;
                }

                if (ideasFeedbackText != '') {
                    let ideasFeedbackCardHTML = feedbackCardTemplate({ feedback_p: ideasFeedbackText });
                    ideasFeedback.innerHTML += ideasFeedbackCardHTML;
                }
            }

            document.getElementById('ratings1').innerHTML = ratingCounts[0];
            document.getElementById('ratings2').innerHTML = ratingCounts[1];
            document.getElementById('ratings3').innerHTML = ratingCounts[2];
            document.getElementById('ratings4').innerHTML = ratingCounts[3];
            document.getElementById('ratings5').innerHTML = ratingCounts[4];

            // Calculate average rating
            let total = 0;
            let count = 0;
            for (let i = 0; i < ratingCounts.length; i++) {
                total += (i + 1) * ratingCounts[i];
                count += ratingCounts[i];
            }

            let averageRating = total / count;
            document.getElementById('averageRating').innerHTML = averageRating.toFixed(2);

            // Update rating chart
            if (ratingChart) {
                ratingChart.destroy();
            }

            ratingChart = new Chart(document.getElementById('ratingChart'), {
                type: 'bar',
                data: {
                    labels: ['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'],
                    datasets: [
                        {
                            label: 'Amount of Ratings',
                            data: ratingCounts
                        }
                    ]
                },
                options: { scales: { y: { ticks: { stepSize: 1 } } } }
            });
        });
});