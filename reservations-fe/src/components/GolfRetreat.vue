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
                <h2 class="heading">Island Golf Retreat</h2>
                <div class="desc">
                  <p>Immerse yourself in the lush greens and breathtaking vistas of the Island Golf Retreat at Emerald
                    Bay Island Resort. Our world-class golf course is designed to challenge and inspire players of all
                    skill levels, offering a unique blend of natural beauty and expertly crafted fairways. Enjoy a
                    leisurely game surrounded by tropical landscapes, with every hole providing a new and exciting
                    experience. Our attentive staff ensures that your golfing experience is nothing short of
                    extraordinary.</p>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="section-slider height-v-about">
                <div id="index12" class="owl-carousel  owl-theme">
                  <div class="item">
                    <img alt="Third slide" src="../assets/images/golf-retreat-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left">
              <div class="img">
                <img src="../assets/images/golf-retreat-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="text">
                <h2 class="heading">Golf Lessons & Pro Shop</h2>
                <div class="desc">
                  <p>Enhance your golfing experience with our comprehensive Golf Lessons and Pro Shop services. Our
                    professional instructors offer personalized lessons to help golfers of all levels improve their
                    skills and enjoy the game even more. Whether you're just starting out or looking to refine your
                    technique, our tailored coaching will guide you towards achieving your goals. After your lesson,
                    visit our Pro Shop to find the latest golf equipment, apparel, and accessories, ensuring you have
                    everything you need for a perfect day on the course at the Island Golf Retreat.</p>
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
