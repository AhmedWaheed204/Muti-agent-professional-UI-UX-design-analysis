import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from src.services.image_service import ImageService
from src.services.analysis_service import AnalysisService
from src.utils.config import Config

def main():
    """Main application entry point."""
    # Initialize configuration
    Config.load_environment()
    
    # Configure page settings
    st.set_page_config(
        page_title="AI Design Analysis Suite",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Set up sidebar
    with st.sidebar:
        st.header("🔑 API Configuration")
        Config.setup_api_key()
    
    # Main application interface
    st.title("Multimodal Design Analysis Platform")
    
    if Config.is_api_configured():
        # File upload section
        st.header("📤 Upload Design Assets")
        col1, col2 = st.columns(2)
        
        with col1:
            design_files = st.file_uploader(
                "Upload Your Designs",
                type=["png", "jpg", "jpeg"],
                accept_multiple_files=True
            )
            
        with col2:
            competitor_files = st.file_uploader(
                "Upload Competitor Designs (Optional)",
                type=["png", "jpg", "jpeg"],
                accept_multiple_files=True
            )
        
        # Analysis configuration
        st.header("🔍 Analysis Parameters")
        analysis_types = st.multiselect(
            "Select Analysis Types",
            ["Visual Design", "User Experience", "Market Analysis"],
            default=["Visual Design"]
        )
        
        context = st.text_area(
            "Additional Context",
            placeholder="Provide information about your target audience, brand guidelines, or specific concerns..."
        )
        
        # Analysis execution
        if st.button("🚀 Run Comprehensive Analysis", type="primary"):
            if design_files:
                try:
                    # Process images
                    design_images = ImageService.process_uploaded_files(design_files)
                    competitor_images = ImageService.process_uploaded_files(competitor_files) if competitor_files else []
                    
                    # Initialize services
                    analysis_service = AnalysisService()
                    
                    # Run analysis
                    results = analysis_service.run_analysis(
                        analysis_types=analysis_types,
                        images=design_images + competitor_images,
                        prompt="Analyze these designs:",
                        context=context
                    )
                    
                    # Display results
                    st.header("📊 Analysis Results")
                    if "visual" in results:
                        st.subheader("🎨 Visual Design Analysis")
                        st.markdown(results["visual"])
                    
                    if "ux" in results:
                        st.subheader("🧑💻 User Experience Evaluation")
                        st.markdown(results["ux"])
                    
                    if "market" in results:
                        st.subheader("🌍 Market Intelligence Report")
                        st.markdown(results["market"])
                    
                    # Cleanup temporary files
                    ImageService.cleanup_files(design_images + competitor_images)
                    
                except Exception as e:
                    st.error(f"Analysis failed: {str(e)}")
            else:
                st.warning("Please upload at least one design file to analyze.")
    else:
        st.info("Please configure your Gemini API key in the sidebar to begin.")

if __name__ == "__main__":
    main()