document.getElementById('invoiceForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const invoiceData = {
    invoiceNumber: document.getElementById('invoiceNumber').value,
    invoiceDate: document.getElementById('invoiceDate').value,
    vendorName: document.getElementById('vendorName').value,
    vendorId: document.getElementById('vendorId').value,
  };

  fetch('/extract-invoice', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ pdf_path: 'path/to/pdf' }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
      document.getElementById('output').innerHTML = 'Invoice processed successfully!';
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
