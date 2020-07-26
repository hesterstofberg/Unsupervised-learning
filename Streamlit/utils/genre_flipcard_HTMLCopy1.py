def genre_flipcard():  
    # change the content to show genres
    # i just copy pasted the person_flipcard_HTML to build the cards
    return """
    <link href="bootstrap-css.css" rel="stylesheet" id="bootstrap-css">

<!-- https://media-exp1.licdn.com/dms/image/C4D03AQGp_j0QNqtI-w/profile-displayphoto-shrink_200_200/0?e=1599091200&v=beta&t=zIdRGpvmpl1A7CRn42AnyV4gH_OLSUbq7BmHqEieiOo -->
<!-- Movie genres -->
<section id="team" class="pb-5">
    <div class="container">
        <h1 class="section-title  text-center">Choose your desired genre</h1>
        </div>
        <div class="row">
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card">
                                    <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">One Flew Over the Cuckoo`s Nest, 1975</h4>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=2WSyJgydTsA">
                                                <i class="fa fa-video-camera"></i>
                                            </a>
                                        </li>
                                    </ul>
                                    <h5 class="card-text">Average rating: 4.22/5</h5>
                                    <p class="card-text">In order to escape the prison labour a prisoner fakes insanity and is shifted to the special ward for the mentally unstable.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Next genre -->
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                    <div class="card-body text-center mt-4">
                                        <h4 class="card-title">Monty Python's Life of Brian, 1979</h4>
                                        <ul class="list-inline ">
                                            <li class="list-inline-item">
                                                <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=TKPmGjVFbrY">
                                                    <i class="fa fa-video-camera"></i>
                                                </a>
                                            </li>
                                        </ul>
                                    <h5 class="card-text">Average rating: 4.0/5</h5>
                                    <p class="card-text">A young man, who was born one stable down and on the same night as Jesus, becomes intrigued by a young rebel.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Next genre -->
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">When We Were Kings, 1996</h4>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=uBauogNmRqY">
                                                <i class="fa fa-video-camera"></i>
                                            </a>
                                        </li>
                                    </ul>
                                    <h5 class="card-text">Average rating: 4.15/5</h5>
                                    <p class="card-text">On October 30, 1974, perhaps the most famous heavyweight championship boxing match of all time took place in Kinshasa, Zaire.</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Next genre -->
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">The Shining, 1980</h4>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=S014oGZiSdI">
                                                <i class="fa fa-video-camera"></i>
                                            </a>
                                        </li>
                                    </ul>
                                    <h5 class="card-text">Average rating: 4.03/5</h5>
                                    <p class="card-text">Jack and his family move into an isolated hotel with a violent past. Living in isolation, Jack begins to lose his sanity, which affects his family members.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Next genre -->
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">Piper, 2016</h4>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=DW8T9nvitLI">
                                                <i class="fa fa-video-camera"></i>
                                            </a>
                                        </li>
                                    </ul>
                                    <h5 class="card-text">Average rating: 4.04/5</h5>
                                    <p class="card-text">Piper is a 2016 computer-animated short film produced by Pixar Animation Studios.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Next genre -->
            <div class="col-xs-12 col-sm-6 col-md-4">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <p><img class=" img-fluid" src="https://github.com/hesterstofberg/flipcards/blob/master/genre_card.png?raw=true" alt="card image"></p>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">Arrival, 2016</h4>
                                    <ul class="list-inline">
                                        <li class="list-inline-item">
                                            <a class="social-icon text-xs-center" target="_blank" href="https://www.youtube.com/watch?v=tFMo3UJ4B4g">
                                                <i class="fa fa-video-camera"></i>
                                            </a>
                                        </li>
                                    </ul>
                                    <h5 class="card-text">Average rating: 4.14/5</h5>
                                    <p class="card-text">Louise Banks, a linguistics expert, along with her team, must interpret the language of aliens who've come to earth in a mysterious spaceship.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            """


