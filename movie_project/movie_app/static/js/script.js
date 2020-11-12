var submitBtn = document.getElementById('submit-btn');
var searchInput= document.getElementById('text');
var movieResults= document.getElementById('movie-results');


const getMovies = async() => {
    const apiurl = 'http://www.omdbapi.com/?apikey=8decb275&s='
    const res = await fetch (`${apiurl}${searchInput.value}`)
    let data = await res.json()
    console.log(data.Search);
    let movies = data.Search

    const showMovie = movies.map((movie)  => {
        return `
        <div class = "container">
               <div class = "row">
                    <div class = "col-md-3">
                        <div class="card">
                            <img class="card-img-top" src="${movie.Poster}" alt="Card image cap">
                            <div class="card-body">
                                <h1 class="card-title">${movie.Title}</h1> 
                                <h4>${movie.Type}</h4>
                                <h4>${movie.Year}</h4>
                                <h4>${movie.imdbID}</h4>   
                            </div>
                        </div>
                    </div>
               </div>
            </div> 
            `   
       }
      
    )
    movieResults.innerHTML = showMovie
  
}

const handleClick = () => {
   getMovies()
}

submitBtn.addEventListener('click', handleClick)

