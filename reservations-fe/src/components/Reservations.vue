<template>
  <div class="reservations-page">
    <h1>Your Reservations</h1>
    <div v-if="reservations.length > 0">
      <ul>
        <li v-for="reservation in reservations" :key="reservation.id">
          <p>Guest: {{ reservation.guest_name }}</p>
          <p>Room: {{ reservation.room_number }}</p>
          <p>Check-in: {{ formatDate(reservation.check_in_date) }}</p>
          <p>Check-out: {{ formatDate(reservation.check_out_date) }}</p>
          <p>Status: {{ reservation.status }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No reservations found.</p>
    </div>
  </div>
  <Footer style="margin-top:420px;"></Footer>
</template>

<script>
import axios from 'axios';
import Footer from "@/components/Footer.vue";

export default {
  name: 'ReservationsPage',
  components: {
    Footer
  },
  data() {
    return {
      reservations: [],
    };
  },
  mounted() {
    this.fetchReservations();
  },
  methods: {
    async fetchReservations() {
      try {
        const response = await axios.get('http://localhost:8000/api/reservations/');
        this.reservations = response.data.data;
      } catch (error) {
        console.error("Error fetching reservations:", error);
      }
    },
    formatDate(dateString) {
      const options = {year: 'numeric', month: 'long', day: 'numeric'};
      return new Date(dateString).toLocaleDateString(undefined, options);
    },
  },
};
</script>

<style scoped>
.reservations-page {
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

h1 {
  margin-bottom: 20px;
}
</style>
