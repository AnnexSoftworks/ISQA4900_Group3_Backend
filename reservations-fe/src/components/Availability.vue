<template>
  <div>
    <h1>Available Rooms</h1>
    <ul>
      <li v-for="room in rooms" :key="room.pk">
        Room {{ room.room_number }}: {{ room.room_type_name }} - ${{ room.rate }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Availability',
  data() {
    return {
      rooms: [],
    };
  },
  methods: {
    async fetchRooms() {
      try {
        const response = await axios.get('api/rooms/');
        this.rooms = response.data.data;
      } catch (error) {
        console.error('Error fetching rooms:', error);
      }
    },
  },
  mounted() {
    this.fetchRooms();
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 0.5rem 0;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
