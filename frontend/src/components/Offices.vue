<template>
  <v-container>
    <h1 style="text-align: center">Oficinas</h1>

    <v-data-table
      :headers="headers"
      :items="offices"
      :items-per-page="5"
      class="elevation-1"
    >
      <template #item.name="{ item }">
        <router-link
          :to="{ path: '/office/' + item.pk, params: { id: item.pk } }"
        >
          {{ item.name }}
        </router-link>
      </template>
      <template v-slot:item.actions="{ item }">
        <router-link
          :to="{ path: '/newreserve/' + item.pk, params: { id: item.pk } }"
        >
          <v-btn class="ma-2" color="primary" dark>
            Crear reserva
            <v-icon dark right> mdi-checkbox-marked-circle </v-icon>
          </v-btn>
        </router-link>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Offices",
  data() {
    return {
      headers: [
        {
          text: "Nombre",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "cant personas", value: "max_people" },
        { text: "Baño", value: "has_bathroom" },
        { text: "Wifi", value: "has_wifi" },
        { text: "Telefono", value: "has_phone" },
        { text: "Crear reserva", value: "actions" },
      ],
      offices: [],
    };
  },

  created() {
    axios
      .get("http://localhost:8000/office/")
      .then((response) => {
        response.data.forEach((element) => {
          if (element.has_phone) {
            element.has_phone = "SI";
          } else {
            element.has_phone = "NO";
          }
          if (element.has_wifi) {
            element.has_wifi = "SI";
          } else {
            element.has_wifi = "NO";
          }
          if (element.has_bathroom) {
            element.has_bathroom = "SI";
          } else {
            element.has_bathroom = "NO";
          }
          this.offices.push(element);
          console.log(element);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
