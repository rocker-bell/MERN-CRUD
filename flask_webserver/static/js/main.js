// document.addEventListener("DOMContentLoaded", function () {

//     const tools = document.querySelectorAll(".tool_list");
//     const sections = document.querySelectorAll(".form_results_container");

//     function SliderFunction(SliderTool) {

//         // Masquer toutes les sections
//         sections.forEach(section => {
//             section.style.display = "none";
//         });

//         // Désactiver tous les outils
//         tools.forEach(tool => {
//             tool.classList.remove("active");
//         });

//         // Afficher la section sélectionnée
//         const selectedSection = document.querySelector(
//             `.form_results_container.${SliderTool}`
//         );

//         if (selectedSection) {
//             selectedSection.style.display = "block";
//         }

//         // Activer le bouton sélectionné
//         const selectedTool = document.querySelector(
//             `.tool_list.${SliderTool}`
//         );

//         if (selectedTool) {
//             selectedTool.classList.add("active");
//         }
//     }

//     // Gestion des clics
//     tools.forEach(tool => {

//         tool.addEventListener("click", function () {

//             const SliderTool = [...tool.classList].find(
//                 className => className !== "tool_list"
//             );

//             SliderFunction(SliderTool);

//         });

//     });

//     // Affichage initial
//     SliderFunction("pgcd-ppcm");

// });


document.addEventListener("DOMContentLoaded", function () {

    const tools = document.querySelectorAll(".tool_list");
    const sections = document.querySelectorAll(".form_results_container");

    // Correspondance entre les opérations Flask et les sections HTML
    const operationSections = {
        "pgcd_ppcm": "pgcd-ppcm",
        "congruence_fermat": "congruence_fermat_bezout",
        "bezout": "congruence_fermat_bezout",
        "indicatrice_euler": "indicatrice_euler",
        "inverse_modulaire": "inverse_modulaire",
        "chiffrements_rsa": "chiffrements_rsa"
    };

    function SliderFunction(SliderTool) {

        // Masquer toutes les sections
        sections.forEach(section => {
            section.style.display = "none";
        });

        // Désactiver tous les outils
        tools.forEach(tool => {
            tool.classList.remove("active");
        });

        // Afficher la section sélectionnée
        const selectedSection = document.querySelector(
            `.form_results_container.${SliderTool}`
        );

        if (selectedSection) {
            selectedSection.style.display = "block";
        }

        // Activer l'élément de navigation
        const selectedTool = document.querySelector(
            `.tool_list.${SliderTool}`
        );

        if (selectedTool) {
            selectedTool.classList.add("active");
        }
    }

    // Gestion des clics dans la navigation
    tools.forEach(tool => {

        tool.addEventListener("click", function () {

            const SliderTool = [...tool.classList].find(
                className => className !== "tool_list" &&
                             className !== "active"
            );

            if (SliderTool) {
                SliderFunction(SliderTool);
            }

        });

    });

    // Récupérer l'opération effectuée par Flask
    const operation = document.body.dataset.operation;

    // Choisir automatiquement la bonne section
    const sectionInitiale = operationSections[operation] || "pgcd-ppcm";

    // Affichage initial
    SliderFunction(sectionInitiale);

});