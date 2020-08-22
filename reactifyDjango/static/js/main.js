let body = document.querySelector('.tweets')


const xhr = new XMLHttpRequest()
let responseType = 'json'
let method = 'GET'
const url = 'http://127.0.0.1:8000/api/tweets'

function likesHandler(tweet_id, currentCount){

    alert(`id:${tweet_id} > Likes: ${currentCount}`)

}

function likeBtn(twt){

    return `<button class='btn btn-primary ' onclick='likesHandler(${twt.id}, ${twt.likes})'>${twt.likes} Likes</button>`

}

function formatTweets(tweet){

    var style = `<div class="col">
                    <p id=${tweet.id}>${tweet.content}</p4>
                </div>`
    style +=        `<div class="col border-bottom mb-2 pb-4"> ${likeBtn(tweet)}
                </div>`
    return style

}

xhr.responseType = responseType

xhr.open(method, url)

xhr.onload = ()=>{
    var serverResponse = xhr.response
    body.innerHTML = '</div class="row"><h4 class="col text-center">Tweets</h4></div>'
    serverResponse.response.forEach((element, i) => {
        console.log(element)
        body.innerHTML += formatTweets(element)

    });
}

xhr.send()




