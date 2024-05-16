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
                    <img alt="Third slide" src="../assets/images/marina-01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-left">
              <div class="text">
                <h2 class="heading">Marina Services</h2>
                <div class="desc">
                  <p>Discover the vibrant heart of Emerald Bay Island Resort at our Marina, where the sparkling waters and pristine yachts create a picturesque setting for adventure and relaxation. Whether you're setting sail on a chartered boat, indulging in water sports, or simply enjoying the stunning views, the Marina offers a perfect blend of excitement and tranquility. Our knowledgeable staff is on hand to assist with all your maritime needs, ensuring a seamless and enjoyable experience.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left col-lg-push-6 col-md-push-6 ">
              <div class="img">
                <img src="../assets/images/marina-02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right col-lg-pull-6 col-md-pull-6">
              <div class="text">
                <h2 class="heading">Sailing and Water Sports</h2>
                <div class="desc">
                  <p>Dive into a world of aquatic fun with our Sailing and Water Sports activities at the Marina. From exhilarating jet ski rides to peaceful paddleboarding and guided sailing tours, there's something for every water enthusiast. Our state-of-the-art equipment and experienced instructors guarantee a safe and thrilling adventure, whether you're a seasoned sailor or a first-time explorer. Embrace the beauty of the open sea and create unforgettable memories at Emerald Bay Island Resort.</p>
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