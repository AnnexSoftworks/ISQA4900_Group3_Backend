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
                    <img alt="Third slide" src="../assets/images/coco-cay01.webp" class="img-responsive">
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-left">
              <div class="text">
                <h2 class="heading">Our History</h2>
                <div class="desc">
                  <p>Emerald Bay Island Resort, in partnership with Royal Caribbean Cruise Lines, stands as a pinnacle
                    of secluded luxury, nestled on the pristine shores of RCCL's Cocoa Cay. Our philosophy weaves the
                    tranquility of an exclusive island getaway with the unmatched convenience of RCCL's impeccable
                    voyages. While we share the island with RCCL, our resort is a world apart—a tranquil enclave
                    dedicated to privacy, luxury, and an immersive natural experience.</p>
                </div>
              </div>
            </div>
          </div>
          <div class="about-item about-right">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6  no-padding-left col-lg-push-6 col-md-push-6 ">
              <div class="img">
                <img src="../assets/images/coco-cay02.webp" alt="#" class="img-responsive">
              </div>
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 no-padding-right col-lg-pull-6 col-md-pull-6">
              <div class="text">
                <h2 class="heading">Tropical Paradise</h2>
                <div class="desc">
                  <p>At Emerald Bay, we believe in creating unforgettable experiences that resonate with the unique
                    essence of our tropical paradise. From the architectural elegance of our accommodations, which
                    harmonize with the island’s natural splendor, to the personalized services designed to indulge your
                    senses, every aspect of the resort is crafted to enchant and soothe. Whether it's a retreat in one
                    of our Coral Studios, an escape to a Garden Bungalow, or a sumptuous stay in our Island Haven
                    Villas, our guests enjoy exclusivity with a view, comfort in the lap of luxury, and nature right at
                    their doorstep. Join us at Emerald Bay, where your island fantasy becomes a reality.</p>
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
