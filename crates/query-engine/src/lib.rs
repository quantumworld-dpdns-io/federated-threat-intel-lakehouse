pub mod iceberg;
pub mod trino;
pub mod vector;

use arrow::record_batch::RecordBatch;
use datafusion::prelude::{DataFrame, SessionContext};
use ftil_core::{FtilError, Result};
use std::sync::Arc;

pub struct QueryEngine {
    ctx: SessionContext,
}

impl QueryEngine {
    pub fn new() -> Self {
        let ctx = SessionContext::new();
        Self { ctx }
    }

    pub fn context(&self) -> &SessionContext {
        &self.ctx
    }

    pub async fn register_table(
        &self,
        name: &str,
        path: &str,
    ) -> Result<()> {
        use datafusion::prelude::ParquetReadOptions;

        self.ctx
            .register_parquet(name, path, ParquetReadOptions::default())
            .await
            .map_err(|e| FtilError::QueryError(e.to_string()))?;
        Ok(())
    }

    pub async fn sql(&self, query: &str) -> Result<Vec<RecordBatch>> {
        let df = self
            .ctx
            .sql(query)
            .await
            .map_err(|e| FtilError::QueryError(e.to_string()))?;

        df.collect()
            .await
            .map_err(|e| FtilError::QueryError(e.to_string()))
    }

    pub async fn execute_dataframe(&self, query: &str) -> Result<DataFrame> {
        self.ctx
            .sql(query)
            .await
            .map_err(|e| FtilError::QueryError(e.to_string()))
    }
}

impl Default for QueryEngine {
    fn default() -> Self {
        Self::new()
    }
}
