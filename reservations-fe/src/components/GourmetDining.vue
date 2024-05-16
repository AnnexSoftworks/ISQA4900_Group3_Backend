<template>
  <section class="banner-tems text-center">
    <div class="container">
      <div class="banner-content">
        <h2 style="text-shadow: 1px 1px 4px #000000; margin-top: -88px;">Emerald Bay Island Resort</h2>
        <p style="text-shadow: 1px 1px 4px #000000;">Where luxury harmonizes with the serene beauty of nature.</p>
      </div>
    </div>
  </section>

  <section class="section-about" style="margin: 44px 0 200px 0;">
    <div class="container">
      <div class="row">
        <div class="wrap-about">
          <div class="about-item">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-left">
              <div class="text">
                <h2 class="heading">Gourmet Dining</h2>
                <div class="desc">
                  <p>Experience the culinary delights of Emerald Bay Island Resort with our exquisite gourmet dining
                    options. Our renowned chefs craft delectable dishes using the freshest local ingredients, providing
                    a feast for the senses. Whether you're savoring a romantic dinner under the stars or enjoying a
                    casual beachfront meal, our gourmet dining experiences are designed to delight every palate.</p>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="section-slider height-v-about">
                <div id="index12" class="owl-carousel  owl-theme">
                  <div class="item">
                    <img alt="Third slide" src="../assets/images/gourmet-dining-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left">
              <div class="img">
                <img src="../assets/images/gourmet-dining-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="text">
                <h2 class="heading">Culinary Workshops</h2>
                <div class="desc">
                  <p>Enhance your culinary skills at Emerald Bay Island Resort with our engaging Culinary Workshops. Led
                    by our expert chefs, these hands-on classes offer guests the opportunity to learn the art of cooking
                    exquisite dishes using local ingredients. Whether you're a seasoned cook or a curious beginner, our
                    workshops provide a fun and educational experience that will leave you inspired and ready to impress
                    in your own kitchen.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Footer></Footer>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Footer
  },
};
</script>

<style>
.header-text {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 220px;
}
</style>
