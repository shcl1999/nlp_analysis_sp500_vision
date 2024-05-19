from src.data_processing import load_data
from src.vectorization import vectorization


if __name__ == '__main__':
    df_vision, df_meta = load_data(save_data=True)
    df_result = vectorization(df_vision, df_meta)
    df_result.to_excel('src/data/vision_similarity_results.xlsx', index=False)