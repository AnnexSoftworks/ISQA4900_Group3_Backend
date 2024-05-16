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
                    <img alt="Third slide" src="../assets/images/fitness-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-left">
              <div class="text">
                <h2 class="heading">Fitness Pavilion</h2>
                <div class="desc">
                  <p>Welcome to the Fitness Pavilion at Emerald Bay Island Resort, where health and wellness are at the
                    forefront of your island experience. Our state-of-the-art facility is equipped with the latest
                    exercise machines and free weights, catering to fitness enthusiasts of all levels. Enjoy a
                    comprehensive workout in a serene environment, with panoramic views that inspire and energize. Our
                    dedicated staff is on hand to assist you, ensuring a safe and effective fitness journey.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left col-lg-push-6 col-md-push-6 ">
              <div class="img">
                <img src="../assets/images/fitness-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right col-lg-pull-6 col-md-pull-6">
              <div class="text">
                <h2 class="heading">Group Classes & Personal Training</h2>
                <div class="desc">
                  <p>Take your fitness routine to the next level with our diverse range of Group Classes and Personal
                    Training sessions. From invigorating yoga and pilates to high-intensity interval training and
                    spinning, our group classes are designed to keep you motivated and engaged. For a more personalized
                    approach, our certified personal trainers offer one-on-one sessions tailored to your individual
                    goals and needs. Whether you prefer the camaraderie of group workouts or the focused attention of a
                    personal trainer, the Fitness Pavilion provides the perfect setting for achieving your health and
                    wellness goals.</p>
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