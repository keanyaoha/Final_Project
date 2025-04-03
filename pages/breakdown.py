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
        # Separate the emissions into two categories (example categories: transport and energy)
        transport_emissions = {k: v for k, v in emissions_filtered.items() if "flight" in k or "car" in k}
        energy_emissions = {k: v for k, v in emissions_filtered.items() if "electricity" in k or "hotel" in k}

        # Plot for transport emissions
        if transport_emissions:
            labels_transport = [activity.replace("_", " ").capitalize() for activity in transport_emissions.keys()]
            values_transport = list(transport_emissions.values())
            fig, ax = plt.subplots()
            ax.pie(values_transport, labels=labels_transport, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### 🚗 Transport Emissions:")
            for label, value in zip(labels_transport, values_transport):
                st.write(f"- **{label}**: {value:.4f} tons")
        
        # Plot for energy emissions
        if energy_emissions:
            labels_energy = [activity.replace("_", " ").capitalize() for activity in energy_emissions.keys()]
            values_energy = list(energy_emissions.values())
            fig, ax = plt.subplots()
            ax.pie(values_energy, labels=labels_energy, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
            st.markdown("### ⚡ Energy Emissions:")
            for label, value in zip(labels_energy, values_energy):
                st.write(f"- **{label}**: {value:.4f} tons")

    else:
        st.info("Your inputs resulted in zero emissions. Try entering some activity data.")

