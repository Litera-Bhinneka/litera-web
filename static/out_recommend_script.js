document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("add-button").addEventListener("click", function() {
        console.log("Button clicked!");
        // Redirect to "show_out_recommendations.html"
        window.location.href = `../outside-recommendation-add/`;
    });
});

async function getRecommendations() {
    return fetch(window.recommendationUrl).then((res) => res.json())
}

async function getUserBooks(){
    const response = await fetch(window.userInventoryUrl);
    const data = await response.json();
    const bookTitles = data.book_titles;
    return bookTitles;
}

async function refreshRecommendations() {
    document.getElementById("card-container").innerHTML = ""
    const recommendations = await getRecommendations()
    console.log(recommendations)
    if (recommendations.length === 0){
        let htmlString = ''
        htmlString += `
        <div class="w-full p-4 mb-4">
            <div class="card text-center">
                <div class="card-text flex items-center justify-center mb-1">
                    There are no recommendations yet, Start recommending now!
                </div>
            </div>
        </div>`
        document.getElementById("card-container").innerHTML = htmlString;
    }else{
        let htmlString = ''
        recommendations.forEach((rec) => {
            let datetime = rec.fields.out_recommendation_date;
            let formattedDate = (new Date(datetime)).toLocaleDateString('en-GB', {
                day: 'numeric',
                month: 'long',
                year: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                hour12: true,
            });
            htmlString += `
            <div class="w-full p-4 mb-4">
                <div class="card">
                    <div class="grid grid-cols-2 gap-4">
                        <div class="card-content">
                            <div class="card-title">If you like to read this book </div>
                            <a href="#" class="flex flex-col items-center rounded-lg md:flex-row md:max-w-xl dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700" style="pointer-events: none;">
                                <div class="flex flex-col justify-between p-4 leading-normal">
                                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${rec.fields.out_book_title}</h5>
                                </div>
                            </a>
                        </div>
                        <div class="card-content">
                            <div class="card-title">You may like to read this book </div>
                            <a href="#" class="flex flex-col items-center rounded-lg md:flex-row md:max-w-xl dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700" style="pointer-events: none;">
                                <div class="flex flex-col justify-between p-4 leading-normal">
                                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${rec.fields.another_out_book_title}</h5>
                                </div>
                            </a>
                        </div>
                    </div>
                        <div class="card-desc">
                            ${rec.fields.out_description}
                        </div>
                        <div class="card-footer">
                            <span class="card-date">recommended by ${rec.fields.out_recommender_name} - ${formattedDate}</span>
                        </div>
                </div>
            </div>`;
            document.getElementById("card-container").innerHTML = htmlString;
        })
    }
}
refreshRecommendations();