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
                <h2 class="heading">
                  Kid's Paradise Club</h2>
                <div class="desc">
                  <p>Welcome to the Kid's Paradise Club at Emerald Bay Island Resort, where young guests embark on a
                    journey of fun and adventure. Our dedicated children's club offers a variety of engaging activities
                    and entertainment options tailored for kids of all ages. From arts and crafts to outdoor games and
                    themed events, every day at the Kid's Paradise Club is filled with excitement and creativity. Our
                    friendly and experienced staff ensure a safe and enjoyable environment, allowing parents to relax
                    and enjoy their time at the resort.</p>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="section-slider height-v-about">
                <div id="index12" class="owl-carousel  owl-theme">
                  <div class="item">
                    <img alt="Third slide" src="../assets/images/kids-club-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left">
              <div class="img">
                <img src="../assets/images/kids-club-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right">
              <div class="text">
                <h2 class="heading">Adventure & Learning Programs
                </h2>
                <div class="desc">
                  <p>At the Kid's Paradise Club, we believe in combining fun with education through our Adventure and
                    Learning Programs. Children can explore the natural wonders of the island with guided nature walks,
                    marine life discoveries, and interactive science projects. Our programs are designed to stimulate
                    curiosity and foster a love for the environment, all while having a blast. Whether building
                    sandcastles on the beach or participating in a treasure hunt, kids will create lasting memories and
                    new friendships in this vibrant and nurturing setting.</p>
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
