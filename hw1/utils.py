import pandas as pd
from scipy import io


# Convenience function to handle data import
def import_mtx_expression_data(mtx_gene_exp_file: str, barcodes_file: str, features_file):
    gene_expression = io.mmread(mtx_gene_exp_file)

    barcodes = pd.read_csv(barcodes_file, header=None)[0]
    features = pd.read_csv(features_file, header=None)[0]

    gene_expression = pd.DataFrame(gene_expression.toarray(), index=barcodes, columns=features)

    return gene_expression
