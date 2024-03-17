const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("comment-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

const approveCommentButtons = document.getElementsByClassName("e");

// Function to get a cookie by name.
/**
 * Retrieves cookie and saves the contained csrf token to a variable for later use
 * Code Taken from Django docs https://docs.djangoproject.com/en/3.2/ref/csrf/
 */
// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }
// const csrftoken = getCookie("csrftoken");
// console.log("CSRF Token: ", csrftoken);

/*
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    let commentContent = document.getElementById(
      `comment${commentId}`
    ).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("data-comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

// // For each "Approve" button:
// for (let button of approveCommentButtons) {
//   // Add a click event listener.
//   button.addEventListener("click", (e) => {
//     console.log("Button clicked");
//     // Prevent the default action.
//     e.preventDefault();

//     // Get the ID of the comment to be approved.
//     let commentId = e.target.getAttribute("data-comment_id");
//     console.log("Comment ID: ", commentId);

//     // Send a request to the server to approve the comment.
//     fetch(`/comment_approve/${commentId}/`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         // Include your CSRF token in the request header.
//         "X-CSRFToken": getCookie("csrftoken"),
//       },
//       body: JSON.stringify({ commentId: commentId }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         // Update the comment's status in the UI.
//         if (data.success) {
//           e.target.innerText = "Approved";
//           e.target.disabled = true;
//         } else {
//           alert("Error approving comment.");
//         }
//       });
//   });
// }
