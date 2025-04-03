import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Emission Breakdown")
st.write("Here is how your estimated carbon footprint breaks down by activity.")

# Make sure emissions are available
if "emission_values" not in st.session_state or not st.session_state.emission_values:
    st.warning("No emission data found. Please fill in your activity data on the main page first.")
else:
    # Get emissions from session state
    emissions_dict = st.session_state.emission_values

    # Filter out zero values for a cleaner chart
    emissions_filtered = {k: v for k, v in emissions_dict.items() if v > 0}

    # If there's valid data to plot
    if emissions_filtered:
        # Separate emissions into categories
        public_transport = {k: v for k, v in emissions_filtered.items() if k in ["Dflight", "Iflight", "diesel_train_local", "diesel_train_long", "electric_train", "bus"]}
        private_transport = {k: v for k, v in emissions_filtered.items() if k in ["petrol_car", "Motorcycle", "ev_scooter", "ev_car", "diesel_car"]}
        food = {k: v for k, v in emissions_filtered.items() if k in ["beef", "beverages", "poultry", "pork", "rice", "sugar", "oils_fats", "meat", "dairy", "fish", "other_food"]}
        others = {k: v for k, v in emissions_filtered.items() if k in ["hotel_stay", "electricity", "water"]}

        # Create pie chart for public transport
        if public_transport:
            labels_public_transport = [activity.replace("_", " ").capitalize() for activity in public_transport.keys()]
            values_public_transport = list(public_transport.values())
            fig, ax = plt.subplots()
            ax.pie(values_public_transport, labels=labels_public_transport, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### 🚉 Public Transport Emissions:")
            for label, value in zip(labels_public_transport, values_public_transport):
                st.write(f"- **{label}**: {value:.4f} tons")

        # Create pie chart for private transport
        if private_transport:
            labels_private_transport = [activity.replace("_", " ").capitalize() for activity in private_transport.keys()]
            values_private_transport = list(private_transport.values())
            fig, ax = plt.subplots()
            ax.pie(values_private_transport, labels=labels_private_transport, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### 🚗 Private Transport Emissions:")
            for label, value in zip(labels_private_transport, values_private_transport):
                st.write(f"- **{label}**: {value:.4f} tons")

        # Create pie chart for food
        if food:
            labels_food = [activity.replace("_", " ").capitalize() for activity in food.keys()]
            values_food = list(food.values())
            fig, ax = plt.subplots()
            ax.pie(values_food, labels=labels_food, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### 🍽️ Food Emissions:")
            for label, value in zip(labels_food, values_food):
                st.write(f"- **{label}**: {value:.4f} tons")

        # Create pie chart for others
        if others:
            labels_others = [activity.replace("_", " ").capitalize() for activity in others.keys()]
            values_others = list(others.values())
            fig, ax = plt.subplots()
            ax.pie(values_others, labels=labels_others, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### 🏠 Other Emissions (Hotel, Electricity, Water):")
            for label, value in zip(labels_others, values_others):
                st.write(f"- **{label}**: {value:.4f} tons")

    else:
        st.info("Your inputs resulted in zero emissions. Try entering some activity data.")

