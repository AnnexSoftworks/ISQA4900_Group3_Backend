<template>
  <footer class="footer-sky">
    <div class="footer-top">
      <div class="container">
        <div class="row">
          <div class="col-xs-12 col-sm-12 col-md-1 col-lg-1">
            <div class="icon-email">
              <a href="#" title="Email"><img src="../assets/images/footer-top-icon.webp" alt="Email"
                                             class="img-responsive"></a>
            </div>
          </div>
          <div class="col-xs-12 col-sm-12 col-md-7 col-lg-5">
            <div class="textbox">
              <form class="form-inline">
                <div class="form-group">
                  <div class="input-group">
                    <input type="email" class="form-control" placeholder="E-Mail Address"
                           aria-label="Search for...">
                    <button class="btn btn-secondary" type="button">
                      <i class="ion-android-send"></i>
                    </button>

                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="col-xs-12 col-sm-12 col-md-4 col-lg-6 text-right">
            <div class="footer-icon-l">
              <a href="#" title="Twitter"><i class="fa fa-twitter" aria-hidden="true"></i></a>
              <a href="#" title="Facebook"><i class="fa fa-facebook-square" aria-hidden="true"></i></a>
              <a href="#" title="Tripadvisor"><i class="fa fa-tripadvisor" aria-hidden="true"></i></a>
              <a href="#" title="Isnstagram"><i class="fa fa-instagram" aria-hidden="true"></i></a>
            </div>
          </div>
        </div>
      </div>
      <!-- /container -->
    </div>
    <!-- /footer-top -->
    <div class="footer-mid">
      <div class="container">
        <div class="row padding-footer-mid">
          <div class="col-xs-12 col-sm-12 col-md-3 col-lg-3">
            <div class="footer-logo text-center list-content">
              <a href="#" title="Skyline"><img src="../assets/images/footer-logo.webp" alt="Image"></a>
            </div>
          </div>
          <div class="col-xs-4 col-sm-4 col-md-2 col-lg-2 col-lg-offset-1 col-md-offset-1  ">
            <div class="list-content">
              <ul>
                <li><a href="#" title="">Home</a></li>
                <li><a href="#" title="">About</a></li>
                <li><a href="#" title="">Amenities</a></li>
                <li><a href="#" title="">Reservations</a></li>
                <li><a href="#" title="">Contact</a></li>
              </ul>
            </div>
          </div>
          <div class="col-xs-4 col-sm-4 col-md-2 col-lg-2 col-lg-offset-1 col-md-offset-1 ">
            <div class="list-content ">
              <ul>
                <li><router-link title="" :to="{name: 'FitnessPavilion'}">Fitness Center</router-link></li>
                <li><a href="#" title="">Restaurants</a></li>
                <li><router-link title="" :to="{name: 'Marina'}">Paradise Marina</router-link></li>
                <li><router-link title="" :to="{name: 'GolfRetreat'}">Golfing</router-link></li>
                <li><router-link title="" :to="{name: 'KidsClub'}">Kid's Club</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-xs-4 col-sm-4 col-md-2 col-lg-2 col-lg-offset-1 col-md-offset-1">
            <div class="list-content ">
              <ul>
                <li><a href="#" title="">FAQS</a></li>
                <li><a href="#" title="">News</a></li>
                <li><a href="#" title="">Photo & Video</a></li>
                <li><a href="#" title="">Restaurant</a></li>
                <li><a href="#" title="">Gift Card</a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6 no-padding">
            Copyright © 2024 by <a href="#" title="">ISQA 4900 Team.</a> Emerald Bay Island Resort
          </div>
          <div class="col-xs-12 col-sm-6 col-md-6 col-lg-6 no-padding">
            <div class="payments text-right">
              <ul>
                <li>
                  <a href="#" title="Paypal"><img src="../assets/images/Home-1/Paypal.png" alt="Paypal"></a>
                </li>
                <li>
                  <a href="#" title="Visa"><img src="../assets/images/Home-1/Visa.png" alt="Visa"></a>
                </li>
                <li>
                  <a href="#" title="Master"><img src="../assets/images/Home-1/Master-card.png" alt="Master"></a>
                </li>
                <li>
                  <a href="#" title="Discover"><img src="../assets/images/Home-1/Discover.png" alt="Discover"></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>


<script>

</script>


<style>

</style>