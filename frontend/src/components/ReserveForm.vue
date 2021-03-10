<template>
  <v-container>
    <h1 style="text-align: center">Crear reserva</h1>
    <div v-if="message.submitted">
      <v-alert v-if="message.type == 201" type="success">
        {{ message.text }}
      </v-alert>
      <v-alert v-else type="warning">
        {{ message.text }}
      </v-alert>
    </div>

    <v-card class="mx-auto my-12 px-4" max-width="600">
      <v-card-text>
        <v-form ref="loginForm" v-model="valid" lazy-validation>
          <v-row>
            <v-col cols="12">
              <span>Cliente</span>
              <v-text-field v-model="reserve.client"></v-text-field>
            </v-col>
            <span>Usuario que tomo la reserva</span>
            <v-col cols="12">
              <v-text-field
                v-model="reserve.user_create_reserve"
              ></v-text-field>
            </v-col>
            <span>Fecha inicio de reserva</span>
            <v-col cols="12">
              <v-menu
                ref="menu_start"
                v-model="menu_start"
                :close-on-content-click="false"
                :return-value.sync="reserve.date_start"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="reserve.date_start"
                    label="Picker in menu"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="reserve.date_start" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu_start = false">
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.menu_start.save(reserve.date_start)"
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12">
              <v-menu
                ref="menu_end"
                v-model="menu_end"
                :close-on-content-click="false"
                :return-value.sync="reserve.date_end"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="reserve.date_end"
                    label="Fecha de finalización"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="reserve.date_end" no-title scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="menu_end = false">
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.menu_end.save(reserve.date_end)"
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-btn x-large block sumbit color="success" @click="createRes">
            Crear Reserva
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "createReserve",

  data() {
    return {
      message: {
        type: "",
        text: "",
        submitted: false,
      },
      menu_start: false,
      menu_end: false,
      modal_end: false,
      moda_start: false,
      reserve: {
        office_id: "",
        client: "",
        user_create_reserve: "",
        date_start: new Date().toISOString().substr(0, 10),
        date_end: new Date().toISOString().substr(0, 10),
      },
    };
  },
  methods: {
    createRes() {
      axios
        .post("http://localhost:8000/reserve/", this.reserve)
        .then((response) => {
          this.message.submitted = true;
          this.message.type = response.status;
          if (response.status == 201) {
            this.message.text = "Se creo la reserva con éxito";
          } else {
            this.message.text = "Ya existe un turno para ese dia";
          }
        })
        .catch((error) => {
          console.log(error);
          this.message.submitted = true;
          this.message.type = 400;
          this.message.text =
            "Verifique que al oficina no tenga turno para la fecha indicada";
        });
    },
  },
  created() {
    this.reserve.office_id = this.$route.params.id;
  },
};
</script>
