<template>
  <section class="banner-tems text-center">
    <div class="container">
      <div class="banner-content">
        <h2 style="margin-top: -88px;">Get in Touch</h2>
        <p>Start Your Journey to Paradise.</p>
      </div>
    </div>
  </section>

  <section class="section-contact" style="margin: 44px 0 200px 0;">
    <div class="container">
      <div class="contact">
        <div class="row">
          <div class="col-md-6 col-lg-5">
            <div class="text">
              <h2>24/7 Island Concierge</h2>
              <p>At Emerald Bay Island Resort, your exceptional experience is our top priority. Whether you have
                questions about your upcoming stay, need assistance with travel arrangements, or simply want to share
                your thoughts, our dedicated team is eager to hear from you. Use the form below to send us a message, or
                reach out directly via phone or email. We pledge to provide a timely and thoughtful response, ensuring
                your journey to our island paradise is nothing short of perfect. For immediate assistance, our customer
                service representatives are available 24/7 to cater to your needs. Connect with us today and take the
                next step in planning your unforgettable island escape.</p>
              <ul>
                <li><i class=" fa ion-ios-location-outline"></i>121 Emerald Bay Dr., Bahamas</li>
                <li><i class="fa fa-phone" aria-hidden="true"></i> (800) 555-8898</li>
                <li><i class="fa fa-envelope-o" aria-hidden="true"></i>contact@emeraldbayresort.com</li>
              </ul>
            </div>
          </div>
          <div class="col-md-6 col-lg-6 col-lg-offset-1">
            <div class="contact-form">
              <form action="send_mail_contact.php" method="post">
                <div class="row">
                  <div class="col-sm-6">
                    <input type="text" class="field-text" name="name" placeholder="Name">
                  </div>
                  <div class="col-sm-6">
                    <input type="text" class="field-text" name="email" placeholder="Phone">
                  </div>
                  <div class="col-sm-12">
                    <input type="text" class="field-text" name="subject" placeholder="Email">
                  </div>
                  <div class="col-sm-12">
                    <textarea cols="30" rows="10" name="message" class="field-textarea"
                              placeholder="Inquiry"></textarea>
                  </div>
                  <div class="col-sm-6">
                    <button type="submit" class="btn btn-room">SEND</button>
                  </div>
                </div>
              </form>
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
