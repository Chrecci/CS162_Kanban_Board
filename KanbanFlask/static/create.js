function ConfirmCancel()
    {
      var x = confirm("Are you sure you want to cancel? All changes will be lost.");
      if (x)
          window.history.back();
    }

