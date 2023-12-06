use pyo3::{
    exceptions::{PyRuntimeError, PyValueError},
    prelude::*,
};

use iroha_crypto::{Algorithm, KeyPair, PrivateKey, PublicKey};

use super::PyMirror;

#[pyclass(name = "PrivateKey")]
#[derive(Clone, derive_more::From, derive_more::Into, derive_more::Deref)]
pub struct PyPrivateKey(pub PrivateKey);

impl PyMirror for PrivateKey {
    type Mirror = PyPrivateKey;

    fn mirror(self) -> PyResult<Self::Mirror> {
        Ok(PyPrivateKey(self))
    }
}

#[pymethods]
impl PyPrivateKey {
    #[new]
    fn new(encoded: &str) -> PyResult<Self> {
        let bytes = hex::decode(encoded)
            .map_err(|e| PyValueError::new_err(format!("Invalid private key: {e}")))?;
        let pk = PrivateKey::from_hex(Algorithm::default(), &bytes)
            .map_err(|e| PyValueError::new_err(format!("Invalid private key: {e}")))?;
        Ok(Self(pk))
    }
}

#[pyclass(name = "PublicKey")]
#[derive(Clone, derive_more::From, derive_more::Into, derive_more::Deref)]
pub struct PyPublicKey(pub PublicKey);

#[pymethods]
impl PyPublicKey {
    #[new]
    fn new(encoded: &str) -> PyResult<Self> {
        let pk = encoded
            .parse()
            .map_err(|e| PyValueError::new_err(format!("Invalid private key: {e}")))?;
        Ok(Self(pk))
    }

    fn __repr__(&self) -> String {
        format!("{:?}", self.0)
    }
}

impl PyMirror for PublicKey {
    type Mirror = PyPublicKey;

    fn mirror(self) -> PyResult<Self::Mirror> {
        Ok(PyPublicKey(self))
    }
}

#[pyclass(name = "KeyPair")]
#[derive(Clone, derive_more::From, derive_more::Into, derive_more::Deref)]
pub struct PyKeyPair(pub KeyPair);

impl PyMirror for KeyPair {
    type Mirror = PyKeyPair;

    fn mirror(self) -> PyResult<Self::Mirror> {
        Ok(PyKeyPair(self))
    }
}

#[pymethods]
impl PyKeyPair {
    #[staticmethod]
    fn generate() -> PyResult<Self> {
        let kp = KeyPair::generate()
            .map_err(|e| PyRuntimeError::new_err(format!("Failed to generate keypair: {e}")))?;
        Ok(PyKeyPair(kp))
    }

    #[getter]
    fn get_private_key(&self) -> PyPrivateKey {
        self.0.private_key().clone().into()
    }

    #[getter]
    fn get_public_key(&self) -> PyPublicKey {
        self.0.public_key().clone().into()
    }

    fn __repr__(&self) -> String {
        format!("{:?}", self.0)
    }
}

pub fn register_items(_py: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_class::<PyPrivateKey>()?;
    module.add_class::<PyPublicKey>()?;
    module.add_class::<PyKeyPair>()?;
    Ok(())
}
