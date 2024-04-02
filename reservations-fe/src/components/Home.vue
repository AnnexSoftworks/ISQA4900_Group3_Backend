<template>
    <div>
        <BookingCarousel>

            <template v-slot:title>
              <h1>
                Welcome to Emerald Bay
              </h1>
              <p>Island Resort & Villas</p>
            </template>
            <BookingForm/>
        </BookingCarousel>
    </div>
</template>

<script>
import BookingCarousel from "@/components/booking/BookingCarousel.vue";
import BookingForm from "@/components/booking/BookingForm.vue";

export default {
    components: {
        BookingCarousel,
        BookingForm
    },
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,700,900');
@import url('https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800');
@import url('https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900');

.title h1 {
  font-family: "Playfair Display", sans-serif;
  font-weight: 400;
  font-size: 3.5em;
  margin-top: 100px;
}

.title h1 span {
  font-family: "Playfair", sans-serif;
  font-weight: 600;
  color: #ff6b6b;
}

.title p {
  font-family: "Poppins", sans-serif;
  font-size: 1.5em;
  text-transform: uppercase;
  margin-top: 4px;
  font-weight: 200;
}
</style>