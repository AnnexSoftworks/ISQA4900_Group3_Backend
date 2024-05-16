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
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="section-slider height-v-about">
                <div id="index12" class="owl-carousel  owl-theme">
                  <div class="item">
                    <img alt="Third slide" src="../assets/images/ocean-spa-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-left">
              <div class="text">
                <h2 class="heading">Ocean Spa</h2>
                <div class="desc">
                  <p>Indulge in the serene luxury of the Ocean Spa at Emerald Bay Island Resort, where the soothing
                    sounds of the waves and the gentle sea breeze create the perfect ambiance for relaxation and
                    rejuvenation. Our spa offers an array of treatments designed to revitalize your body and spirit,
                    including therapeutic massages, invigorating body scrubs, and nourishing facials. Each session is
                    personalized to ensure your utmost comfort and satisfaction, allowing you to experience unparalleled
                    tranquility and rejuvenation.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left col-lg-push-6 col-md-push-6 ">
              <div class="img">
                <img src="../assets/images/ocean-spa-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right col-lg-pull-6 col-md-pull-6">
              <div class="text">
                <h2 class="heading">Wellness Center</h2>
                <div class="desc">
                  <p>At the Wellness Center, we believe that true well-being encompasses both physical and mental
                    health. Our state-of-the-art facility offers a comprehensive range of wellness programs and
                    activities designed to nurture your mind, body, and soul. From guided yoga sessions on the beach at
                    sunrise to personalized fitness training and holistic health consultations, our experienced staff is
                    dedicated to helping you achieve your wellness goals.</p>
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