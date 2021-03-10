<template>
  <v-container>
    <h1 style="text-align: center">{{ office.name }}</h1>

    <v-card class="mx-auto my-12 px-4" max-width="600">
      <v-card-text>
        <v-form ref="loginForm" v-model="valid" lazy-validation>
          <v-row>
            <v-col cols="12">
              <span>Nombre de la oficina</span>
              <v-text-field v-model="office.name" disabled></v-text-field>
            </v-col>
            <v-col cols="12">
              <span>Código</span>
              <v-text-field v-model="office.cod_int" disabled></v-text-field>
            </v-col>
            <span>Máximo de gente</span>
            <v-col cols="12">
              <v-text-field v-model="office.max_people" disabled></v-text-field>
            </v-col>
            <span>Tiene baño privado</span>
            <v-col cols="12">
              <v-text-field
                v-model="office.has_bathroom"
                disabled
              ></v-text-field>
            </v-col>
            <span>Tiene wifi</span>
            <v-col cols="12">
              <v-text-field v-model="office.has_wifi" disabled></v-text-field>
            </v-col>
            <v-col cols="12">
              <span>Tiene Telefono</span>
              <v-text-field v-model="office.has_phone" disabled></v-text-field>
            </v-col>
            <v-col cols="12">
              <span>Usuario a cargo</span>
              <v-text-field
                v-model="office.user_in_charge"
                disabled
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>
    </v-card>

    <v-data-table
      :headers="headers"
      :items="reserves"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="dialogDelete = true"> mdi-delete </v-icon>
      </template>
    </v-data-table>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Seguro que desea eliminar la reserva?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "Reserve",

  data() {
    return {
      dialogDelete: false,
      headers: [
        {
          text: "Cliente",
          align: "start",
          sortable: false,
          value: "client",
        },
        { text: "Fecha inicio reserva", value: "date_start" },
        { text: "Fecha fin de reserva", value: "date_end" },
        { text: "Acciones", value: "actions" },
      ],
      reserves: [],
      editedIndex: -1,
      office: {
        name: "",
        max_people: "",
        cod_int: "",
        user_in_charge: "",
        has_phone: "",
        has_bathroom: "",
        has_wifi: "",
      },
    };
  },

  watch: {
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  methods: {
    deleteItemConfirm() {
      let item = this.reserves.splice(this.editedIndex, 1);

      axios.delete("http://localhost:8000/reserve/" + item[0].pk).then(() => {
        this.closeDelete();
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedIndex = -1;
      });
    },
  },
  created() {
    axios
      .get("http://localhost:8000/office/" + this.$route.params.id)
      .then((response) => {
        this.office.name = response.data[0].name;
        this.office.max_people = response.data[0].max_people;
        this.office.cod_int = response.data[0].cod_int;
        this.office.user_in_charge = response.data[0].user_in_charge;
        if (response.data[0].has_phone == "True") {
          this.office.has_phone = "SI";
        } else {
          this.office.has_phone = "NO";
        }
        if (response.data[0].has_wifi == "True") {
          this.office.has_wifi = "SI";
        } else {
          this.office.has_wifi = "NO";
        }
        if (response.data[0].has_bathroom == "True") {
          this.office.has_bathroom = "SI";
        } else {
          this.office.has_bathroom = "NO";
        }
      });

    axios
      .get(
        "http://localhost:8000/reserve/" +
          this.$route.params.id +
          "/get_last_reserves/"
      )
      .then((response) => {
        this.reserves = response.data;
      });
  },
};
</script>
