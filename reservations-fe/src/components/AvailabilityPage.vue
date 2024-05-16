<template>
  <div class="availability-page">
    <h1>Available Rooms</h1>
    <div v-if="availableRooms.length > 0">
      <ul>
        <li v-for="room in availableRooms" :key="room.pk">
          <p>Room Number: {{ room.room_number }}</p>
          <p>Room Type: {{ room.room_type_name }}</p>
          <p>Guest Limit: {{ room.guest_limit }}</p>
          <p>Rate: ${{ room.rate }}</p>
          <button @click="bookRoom(room.pk)">Book this room</button>
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No available rooms found.</p>
    </div>
  </div>
  <Footer style="margin-top: 500px;"></Footer>
</template>

<script>
import axios from 'axios';
import Footer from "@/components/Footer.vue";

export default {
  name: 'AvailabilityPage',
  components: { Footer },
  data() {
    return {
      availableRooms: [],
    };
  },
  mounted() {
    this.checkAvailability();
  },
  methods: {
    async checkAvailability() {
      try {
        const response = await axios.post('http://localhost:8080/api/check_availability/');
        console.log("Response data:", response.data);
        this.availableRooms = response.data.available_rooms;
      } catch (error) {
        console.error("Error checking room availability:", error);
      }
    },
    async bookRoom(roomId) {
      try {
        const response = await axios.post('http://localhost:8080/api/create_reservation/', {
          room_id: roomId,
        });
        this.$router.push({ name: 'ReservationsPage' });
      } catch (error) {
        console.error("Error booking room:", error);
      }
    },
  },
};
</script>

<style scoped>
.availability-page {
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
